import React from 'react';
import { io } from 'socket.io-client';
import './App.css';
import { StockSearch } from './StockSearch.js';
import { StockLoad } from './StockLoad.js';

const socket = io();

function App() {
  return (
    <div>
      {<StockSearch socket={socket}/>}
      {<StockLoad socket={socket}/>}
    </div>
  );
}

export default App;
