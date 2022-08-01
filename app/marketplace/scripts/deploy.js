// This is a script for deploying your contracts.
async function main() {
    // This is just a convenience check
    if (network.name === "hardhat") {
        console.warn(
            "You are trying to deploy a contract to the Hardhat Network, which" +
            "gets automatically created and destroyed every time. Use the Hardhat" +
            " option '--network localhost'"
        );
    }

    // ethers is available in the global scope
    const [deployer] = await ethers.getSigners();
    console.log(
        "Deploying the contracts with the account:",
        await deployer.getAddress()
    );

    console.log("Account balance:", (await deployer.getBalance()).toString());

    // const Token = await ethers.getContractFactory("Token");
    // const token = await Token.deploy();
    // await token.deployed();

    const Marketplace = await ethers.getContractFactory("Marketplace");
    const marketplace = await Marketplace.deploy();
    await marketplace.deployed();
    console.log("Marketplace contract address:", marketplace.address);

    // We also save the contract's artifacts and address in the frontend directory
    saveFrontendFiles(marketplace);
}

function saveFrontendFiles(marketplace) {
    const fs = require("fs");
    const contractsDir = __dirname + "/../artf";

    if (!fs.existsSync(contractsDir)) {
        fs.mkdirSync(contractsDir);
    }

    fs.writeFileSync(
        contractsDir + "/contract-address.json",
        JSON.stringify({ Marketplace: marketplace.address }, undefined, 2)
    );

    const MarketplaceArtifact = artifacts.readArtifactSync("Marketplace");

    fs.writeFileSync(
        contractsDir + "/Marketplace.json",
        JSON.stringify(MarketplaceArtifact, null, 2)
    );
}

// export { deploy };

main()
.then(() => process.exit(0))
.catch((error) => {
  console.error(error);
  process.exit(1);
});