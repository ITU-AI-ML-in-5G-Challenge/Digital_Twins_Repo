// Connect to the IPFS API
import { create } from "ipfs-http-client";

// instantiate an ipfs http client
async function ipfsClient() {
    const client = await create(
        {
            host: 'localhost',
            port: 5001,
            protocol: "http"
        }
    );
    return client;
}

async function upload(client, file){
    let result = client.add(file);

    return result;

}

export {ipfsClient, upload};