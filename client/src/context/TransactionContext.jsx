import React, { useEffect, useState } from "react";
import { ethers } from "ethers";
import { contractABI, contractAddress } from "../constant";
import { createContext } from "react";

export const TransactionContext = createContext();

const { ethereum } = window;

const EthereumContract = () => {
    const provider = new ethers.providers.Web3Provider(ethereum);
    const signer = provider.getSigner();
    const transactionContract = new ethers.Contract(
        contractAddress,
        contractABI,
        signer
    );

    console.log({
        provider,
        signer,
        transactionContract,
    });
};

export const TransactionProvider = ({ children }) => {
    return (
        <TransactionContext.Provider value={{value: 'test'}}>
            {children}
        </TransactionContext.Provider>
    );
};
