import React, { Component } from 'react';
import { render } from 'react-dom';

import '../css/style.css';

import keenImage from '../assets/keen.png';

import Goal from './components/Goal.js';

export default class App extends Component {
    render() {
        return (
            <div>
              <div>NRQ!</div>
              <div>Create End Goal</div>
              <Goal></Goal>
            </div>
        )
    }
}

render(<App />, document.getElementById('app'));