import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class Root extends Component {
  render() {
    return(
      <h1>Hello WebApp from React</h1>
    )
  }
}



document.addEventListener("DOMContentLoaded", () => {
  console.log("YEA")

  let container = document.getElementById('app');
  let component = <Root/>;
  ReactDOM.render(component, container);
})
