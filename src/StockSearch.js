import React from 'react';
import logo from './logo.svg';
import { useState, useRef, useEffect } from 'react';
import './App.css';


export function StockSearch(prop) {
    const socket = prop.socket;
    const inputRef = useRef(null);
    
    function onClickButton(){
        if(inputRef.current.value !== null && inputRef.current.value !== ""){
            const stock = inputRef.current.value;
            socket.emit('search', { stock: stock });
        }
    }
    return (
        <div>
            Enter Stock symbol here: <input ref={inputRef} type='text' />
            <button onClick={onClickButton}>Send</button>
        </div>
      );
}
      //{<StockLoard socket={socket}/>}