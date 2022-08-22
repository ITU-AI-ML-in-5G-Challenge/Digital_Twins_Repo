// ethers to interact with the Ethereum network and our contract
import { ethers } from "ethers";
// import {hre} from "hardhat";

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
const w = getTestWallet();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.post("/upload", async function (req, res) {

    const file = req.body.file;
    const fileJson = JSON.parse(file);
    console.log("This is the sent file: ", file);
    const result = await uploadFile(file);
    res.json({ cid: result.path });
    console.log(fileJson.type);
    const resp = await send(fileJson);
    if (resp) console.log("File sent correctly.");
});

async function uploadFile(file) {

    const marketplaceSC = new ethers.Contract(
        contractAddress.Marketplace,
        MarketplaceArtifact.abi,
        w
    );

    // console.log(marketplaceSC)
    if (w && marketplaceSC) {
        const ipfsIp = process.env.IPFS_IP;
        // Connect to the IPFS API
        const client = await create(
            {
                host: ipfsIp,
                port: 5001,
                protocol: "http"
            }
        );

        const result = await client.add(file, { onlyHash: true });
        console.log("File hash computed:", result.path);
        console.log("File result with only hash:", result);

        if (result) {
            try {
                const tx = await marketplaceSC.uploadFile(result.path, file.id);

                // Wait for tx to be mined and get receipt.
                const receipt = await tx.wait();

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
                const f = await client.add(file);
                if (f) {
                    console.log("File successfully uploaded to IPFS: ", result);
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
            // We copy the options object to send another post to the Evolution Controller
            optionsEvolCtr = options;
            optionsEvolCtr.uri = 'http://172.16.239.11:6004/exp_rep';
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
    return;

}

function getTestWallet() {
    // Test Account: Account #16: 0x2546BcD3c84621e976D8185a91A922aE77ECEc30 (10000 ETH) 
    // Private Key: 0xea6c44ac03bff858b476bba40716402b03e41b8e97e276d1baec7c37d42484a0

    const privateKey = process.env.PRIV_KEY;

    // const privateKey = "0xea6c44ac03bff858b476bba40716402b03e41b8e97e276d1baec7c37d42484a0";
    const wallet = new ethers.Wallet(privateKey, ethers.provider);

    console.log("Account in use: ", wallet.address);

    return wallet;
}

function getWallet(){

}

// Server listening to PORT 3000
app.listen(3000);
