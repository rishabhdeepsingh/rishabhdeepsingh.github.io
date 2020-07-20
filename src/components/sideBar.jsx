import React, { Component } from "react";
import SideNav, { NavIcon, NavItem, NavText } from "@trendmicro/react-sidenav";
import HomeTwoToneIcon from "@material-ui/icons/HomeTwoTone";
import PictureAsPdfTwoToneIcon from "@material-ui/icons/PictureAsPdfTwoTone";
import AlgovisualIcon from "../images/algorithm.svg";
import "@trendmicro/react-sidenav/dist/react-sidenav.css";

class SideBar extends Component {
  render() {
    return (
      <SideNav onSelect={this.props.onSelect}>
        <SideNav.Toggle />
        <SideNav.Nav defaultSelected="home">
          <NavItem eventKey="/">
            <NavIcon>
              <HomeTwoToneIcon />
            </NavIcon>
            <NavText>Home</NavText>
          </NavItem>
          <NavItem eventKey="resume.pdf">
            <NavIcon>
              <PictureAsPdfTwoToneIcon />
            </NavIcon>
            <NavText>Resume</NavText>
          </NavItem>
          <NavItem eventKey="Algovisual">
            <NavIcon>
              <img
                src={AlgovisualIcon}
                width={40}
                height={40}
                alt="Algovisual"
              />
            </NavIcon>
            <NavText>AlgoVisual</NavText>
          </NavItem>
        </SideNav.Nav>
      </SideNav>
    );
  }
}

export { SideBar };
