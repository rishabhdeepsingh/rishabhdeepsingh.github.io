import React, { Component } from "react";

const styles = {
  color: "red",
  alignment: "center",
  "padding-left": "45%",
};

class User extends Component {
  render() {
    return (
      <div style={styles}>
        <h1>User Page</h1>
      </div>
    );
  }
}

export default User;
