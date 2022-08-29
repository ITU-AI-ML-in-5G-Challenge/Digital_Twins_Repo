// Import ethers to interact with the Ethereum network and our contract
import { ethers } from "ethers";

import express from "express";
import bodyParser from "body-parser";
// import { ipfsClient } from "./ipfs";
import request from "request-promise";

import { create } from "ipfs-http-client";

// Contract artifacts
import MarketplaceArtifact from "./artf/Marketplace.json" assert {type: "json"};
import contractAddress from "./artf/contract-address.json" assert {type: "json"};

// This is an error code that indicates that the user canceled a transaction
const ERROR_CODE_TX_REJECTED_BY_USER = 4001;

const app = express();
const w = getWallet();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.post("/upload", async function (req, res) {

    const file = req.body.file;
    const fileJson = JSON.parse(file);
    console.log("=================== NEW FILE RECEIVED ===================");
    console.log("File type: ", fileJson.type);
    console.log("Content: ", file);

    // Upload file to the Marketplace (IPFS + Ethereum)
    const result = await uploadFile(file);

    // We add the CID (Content Identifier) of the uploaded file to the response
    res.json({ cid: result.path });

    // We send the file to the corresponding nodes.  
    const resp = await send(fileJson);

    if (resp) console.log("FILE WAS SENT SUCCESSFULLY");
});

async function uploadFile(file) {

    const marketplaceSC = new ethers.Contract(
        contractAddress.Marketplace,
        MarketplaceArtifact.abi,
        w
    );

    // marketplaceSC.on('FileUploaded', (fileNumber, cid, name, objectType, uploader) => {
    //     console.log({
    //         fileNumber: fileNumber,
    //         cid: cid,
    //         name: name,
    //         objectType: objectType,
    //         uploader: uploader
    //     });
    // });

    if (w && marketplaceSC) {

        // We load the IP of the IPFS container from the environment variable named "IPFS_IP"
        const ipfsIp = process.env.IPFS_IP;

        // Connect to the IPFS API
        const client = await create(
            {
                host: ipfsIp,
                port: 5001,
                protocol: "http"
            }
        );
        // Before uploading to IPFS, we compute only the CID to be registered in Ethereum.
        const result = await client.add(file, { onlyHash: true });
        console.log("File CID computed:", result.path);
        // console.log("File result with only hash:", result);

        if (result) {
            try {
                const tx = await marketplaceSC.uploadFile(result.path, file.id);

                // Wait for tx to be mined and get receipt.
                const receipt = await tx.wait();
                // console.log(receipt.logs);

                if (receipt.status === 0) {
                    // We can't know the exact error that made the transaction fail when it
                    // was mined, so we throw this generic one.
                    throw new Error("Transaction failed.");
                }
            } catch (error) {

                // We check the error code to see if this error was produced because the
                // user rejected a tx. If that's the case, we do nothing.
                if (error.code === ERROR_CODE_TX_REJECTED_BY_USER) {
                    console.log("Canceled by user");
                    return;
                }

            } finally {
                // If we get here, the transaction was succesful.
                console.log("File upload was successfully registered in the chain !");
                // const returnedCID = await marketplaceSC.getLastFile();
                // console.log("Returned CID: ", returnedCID);
                // marketplaceSC.on("FileUploaded", () => {console.log("FileUploaded")})
                // let event = marketplaceSC.FileUploaded(function(error, result) {
                //     if(!error)console.log(result);
                // });

                // Only after the transaction has succeeded the file is added to IPFS.
                const f = await client.add(file);

                if (f) {
                    console.log("File successfully uploaded to IPFS !");
                    console.log("File: ", result);
                    return f;
                }

            }
        }

    }

}

async function send(file) {
    let options = {
        method: "POST",
        uri: undefined,
        body: file,
        // Automatically stringifies
        // the body to JSON 
        json: true
    };
    let optionsEvolCtr = undefined;
    switch (file.type) {
        case 'controller':
            options.uri = 'http://172.16.239.21:6001/controller';
            break;
        case 'exp_rep':
            // Experimentation report is sent to the Curation Controller
            options.uri = 'http://172.16.239.41:6003/exp_rep';

            // We also send the report to the Evolution Controller, closing the loop.
            // We make a deep copy of the options object to send another post to the Evolution Controller
            optionsEvolCtr = JSON.parse(JSON.stringify(options));
            optionsEvolCtr.uri = 'http://172.16.239.11:6004/exp_rep';

            console.log(options, optionsEvolCtr);
            break;
        case 'ptr_ctr':
            console.log("Protected controller detected. Doesn't need to be sent.");
            return;
        default:
            console.log(`Error sending file: type "${file.type}" is not recognized.`);
            return;
    }
    const sendrequest = await request(options)

        // The parsedBody contains the data
        // sent back from the Flask server 
        .then(function (parsedBody) {
            // console.log(parsedBody);
            return parsedBody;
        })
        .catch(function (err) {
            console.log(err);
        });
    if (optionsEvolCtr) {
        const sendrequestEvolCtr = await request(optionsEvolCtr)

            // The parsedBody contains the data
            // sent back from the Flask server 
            .then(function (parsedBody) {
                // console.log(parsedBody);
                return parsedBody;
            })
            .catch(function (err) {
                console.log(err);
            });
    }
    return sendrequest || sendrequestEvolCtr;

}
// Get the corresponding wallet from the environment variable PRIV_KEY to sign transactions. 
function getWallet() {

    const privateKey = process.env.PRIV_KEY;
    
    console.log("Provider", ethers.provider);
    const wallet = new ethers.Wallet(privateKey, ethers.provider);

    console.log("Account in use: ", wallet.address);

    return wallet;
}

// Server listening to PORT 3000
app.listen(3000);
