import React from 'react';
import './App.css';

export function Stock(prop){
    return (
        <tr>
        <td>{prop.date}</td>
        <td>{prop.open}</td>
        <td>{prop.close}</td>
        <td>{prop.high}</td>
        <td>{prop.low}</td>
        <td>{prop.volume}</td>
        </tr>
    );
}