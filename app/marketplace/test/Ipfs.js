const { expect } = require("chai");

const { ethers } = require("hardhat");

describe("IPFS contract", function () {
    it("File count is equal to number of files uploaded", async function () {
        const Ipfs = ethers.ContractFactory("Ipfs");
        const hardhatIpfs = await Ipfs.deploy();
        let cidList = [QmabZYERV4d3qWTnpxNKWvjxYau7TVSq8vKiFgtvLa2U5o, QmabZYERV4d3qWTnpxNKWvjxYau7TVSq8vKiFgtvLa2ER0];

        for (cid of cidList){
            await hardhatIpfs.registerFile(cid);
        }
        expect(await hardhatIpfs.fileCount()).to.equal(cidList.length);
    })
})