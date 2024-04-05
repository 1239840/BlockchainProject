// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DigitalIdentityManagement {
    struct Identity {
        string name;
        address owner;
        bool verified;
    }

    mapping(address => Identity) public identities;
    address public contractOwner;

    event IdentityCreated(address indexed owner, string name);
    event IdentityVerified(address indexed owner);

    constructor() {
        contractOwner = msg.sender;
    }

    function createIdentity(string memory _name) public {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(identities[msg.sender].owner == address(0), "Identity already exists");

        identities[msg.sender] = Identity(_name, msg.sender, false);
        emit IdentityCreated(msg.sender, _name);
    }

    function verifyIdentity(address _owner) public {
        require(msg.sender == _owner || msg.sender == contractOwner, "Only the owner or contract owner can verify identity");
        require(identities[_owner].owner != address(0), "Identity does not exist");

        identities[_owner].verified = true;
        emit IdentityVerified(_owner);
    }

    function getIdentity(address _owner) public view returns (string memory, address, bool) {
        Identity memory identity = identities[_owner];
        return (identity.name, identity.owner, identity.verified);
    }

    function getContractOwner() public view returns (address) {
        return contractOwner;
    }
}
