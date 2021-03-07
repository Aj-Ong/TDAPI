import React from 'react';
import logo from './logo.svg';
import { useState, useEffect } from 'react';
import { io } from 'socket.io-client';
import { Stock } from './Stock.js'
import './App.css';

export function StockLoad(prop) {
    const socket = prop.socket;
    const [datelst, changedatelst] = useState([]);
    const [openlst, changeopenlst] = useState([]);
    const [closelst, changecloselst] = useState([]);
    const [highlst, changehighlst] = useState([]);
    const [lowlst, changelowlst] = useState([]);
    const [volumelst, changevolumelst] = useState([]);
    const [symbol, changeSymbol] = useState([]);
  
    useEffect( () => {
        socket.on('StockCall', (data) => {
            changedatelst(data.datelst);
            changeopenlst(data.openlst);
            changecloselst(data.closelst);
            changehighlst(data.highlst);
            changelowlst(data.lowlst);
            changevolumelst(data.volumelst);
            changeSymbol(data.symbol);
        });
    }, []);
  
    return (
    <div>
        <h1>{symbol}</h1>
        <table>
            <thead>
              <tr>
                <th scope="col">Dates</th>
                <th scope="col">Open</th>
                <th scope="col">Close</th>
                <th scope="col">Highs</th>
                <th scope="col">Lows</th>
                <th scope="col">Volumes</th>
                
              </tr>
            </thead>
            <tbody>
              {datelst.map((item, index) => <Stock key={index} date={item} open={openlst[index]} close={closelst[index]} high={highlst[index]} low={lowlst[index]} volume={volumelst[index]} />)}
            </tbody>
        </table>
    </div>
  );
}