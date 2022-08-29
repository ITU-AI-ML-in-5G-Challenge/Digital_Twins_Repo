//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// We import this library to be able to use console.log
import "hardhat/console.sol";

contract Marketplace {
    // A structure for registering files to the blockchain
    struct File {
        // Number of file uploaded into the Marketplace. For ease of access.
        uint256 fileNumber;
        // IPFS Content ID (CID)
        string cid;
        // Name of the file
        string name;
        // Type of the object: controller, exp_rep...
        string objectType;
        // Account that uploaded the file. The payable modifier specifies that it can use .transfer(..) and .send(..) (i.e. send and receive funds)
        address payable uploader;
    }
    // Total number of files registered in the chain and uploaded to IPFS
    uint256 public fileCount = 0;

    // fileCount (i.e. file number) => file
    mapping (uint256 => File) public fileStore;

    // Event for informing off-chain apps when a file is uploaded.
    event FileUploaded(
        uint256 fileNumber,
        string cid,
        string name,
        string objectType,
        address payable uploader
    );

    // A function to register files into the chain
    function uploadFile(
        string memory _cid,
        string memory _name,
        string memory _objectType
    ) public {
        // Input validation
        require(bytes(_cid).length > 0);
        require(bytes(_name).length > 0);
        // msg.sender is different from the genesis address
        require(msg.sender != address(0));

        // Mappings in solidity don't have a length attribute
        // Increase the file count
        fileCount++;

        fileStore[fileCount] = File(
            fileCount,
            _cid,
            _name,
            _objectType,
            payable(msg.sender) // casting to address payable
        );

        // Sent to and read by the js application
        emit FileUploaded(
            fileCount,
            _cid,
            _name,
            _objectType,
            payable(msg.sender)
        );
    }

    function getLastFile()
        external
        view
        returns (string memory cid)
    {

        return fileStore[fileCount].cid;
        // console.log("File struct in ETH: ", uploadedFiles[account]);
        // return uploadedFiles[account];
    }
}
