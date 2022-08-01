//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// We import this library to be able to use console.log
import "hardhat/console.sol";

contract Ipfs {
    // An address type variable is used to store ethereum accounts.
    address public owner;
    // Solidity mappings don't have length attribute, so we control the number of files with a counter
    uint256 public fileCount = 0;

    // The CID (content id) of a file
    string ipfsCid;

    // struct File {
    //     uint256 fileId;
    //     string filePath;
    //     string fileName;
    //     string fileType;
    //     address payable uploader;
    //     // size in bytes
    //     // uint256 size;
    //     //uint256 time; // block.timestamp
    // }

    // mapping(uint256 => File) public uploadedFiles;

    // Map file names to cids
    // mapping(string => string) filesCids;

    // Mapping of files owned by account by CID.
    mapping(address => string[]) files;

    // event FileUploaded(
    //     uint256 fileId,
    //     string filePath,
    //     string fileName,
    //     string fileType,
    //     address payable uploader
    // );

    /**
     * A funtion to register a file upload
     * The `external` modifier makes a function *only* callable from outside the contract.
     **/
    function registerFile(string memory cid) external {
        ipfsCid = cid;
        files[msg.sender].push(cid);
        fileCount = files[msg.sender].length;
    }
    // function registerFile(
    //     string memory _filePath,
    //     uint256 _fileSize,
    //     string memory _fileType,
    //     string memory _fileName
    // ) public {
    //     require(bytes(_filePath).length > 0);
    //     require(bytes(_fileType).length > 0);
    //     require(bytes(_fileName).length > 0);
    //     require(_fileSize > 0);
    //     require(msg.sender != address(0));

    //     fileCount++;

    //     uploadedFiles[fileCount] = File(
    //         fileCount,
    //         _filePath,
    //         _fileName,
    //         _fileType,
    //         payable(msg.sender)
    //     );

    //     emit FileUploaded(
    //         fileCount,
    //         _filePath,
    //         _fileName,
    //         _fileType,
    //         payable(msg.sender)
    //     );
    // }

    function getCid() public view returns (string memory cid) {
        return ipfsCid;
    }

    function getFiles(address account)
        external
        view
        returns (string[] memory fileList)
    {
        return files[account];
        // console.log("File struct in ETH: ", uploadedFiles[account]);
        // return uploadedFiles[account];
    }
}
