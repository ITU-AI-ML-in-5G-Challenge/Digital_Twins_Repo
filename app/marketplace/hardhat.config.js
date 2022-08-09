require("@nomicfoundation/hardhat-toolbox");
require("@nomicfoundation/hardhat-chai-matchers");
require("@nomiclabs/hardhat-ethers");

// Task to give ETH to a specific account. For testing purposes.
require("./tasks/faucet");
const besuIP = process.env.BESU_IP;
/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.9",
  defaultNetwork: "localhost",
  networks: {
    hardhat: {
      chainId: 31337
    },
    localhost: {
      url: "http://127.0.0.1:8545"
    },
    besu: {
      chainId: 1337,
      url: `http://${besuIP}:8545`
    }
  }
};