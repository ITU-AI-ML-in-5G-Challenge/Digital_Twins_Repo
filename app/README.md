# FGAN_Digital_Twins
FGAN Buil-a-Thon 2022 project

## Quick Start
### Prerequisites
* Node.js and npm: https://nodejs.org/en/
* IPFS (follow the instructions at: https://docs.ipfs.io/install/)

> After downloading IPFS, start the daemon with the following command:
>
> ```sh
> ipfs daemon&
> ```
### Installation
Start by cloning the repository and installing its dependencies:

```sh
git clone https://github.com/FGAN-Digital-Twins/FGAN_Digital_Twins.git
cd FGAN_Digital_Twins/marketplace
npm install
```

Once installed, run Hardhat's testing network from the marketplace folder:

```sh
npx hardhat node
```

Then, on a new terminal, go to the repository's root folder and run this to
deploy your contract:

```sh
npx hardhat run scripts/deploy.js --network localhost
```

> Note: There's [an issue in `ganache-core`](https://github.com/trufflesuite/ganache-core/issues/650) that can make the `npm install` step fail. 
>
> If you see `npm ERR! code ENOLOCAL`, try running `npm ci` instead of `npm install`.
