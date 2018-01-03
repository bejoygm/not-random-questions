import React, { Component } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';


class Goal extends Component {
  constructor(props) {
    super(props);
    
    this.state = {
      goalName: ''
    }
    
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    axios.post('http://localhost:8000/goal', {name: 'hula'}).then((data) => {
      console.log(data);
    })
  }

  handleChange(event) {
    let value = event.target.value;
    this.setState(() => {
      return {
        goalName: value
      }
    })
  }

  render() {
    return (
      <form className="column" onSubmit={this.handleSubmit}>
        <label className="header" htmlFor="goal">
          Goal
        </label>
        <input
          id="goal"
          placeholder="Create an End Goal"
          type="text"
          autoComplete="off"
          value={this.state.goalName}
          onChange={this.handleChange}
        />
        <button
          className="button"
          type="submit"
          disabled={!this.state.goalName}
        >
          Submit
        </button>
      </form>
    )
  }
}

module.exports = Goal
