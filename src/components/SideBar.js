import React, {Component} from "react";
import SideNav, {NavIcon, NavItem, NavText} from "@trendmicro/react-sidenav";
import HomeTwoToneIcon from '@material-ui/icons/HomeTwoTone';
import PictureAsPdfTwoToneIcon from '@material-ui/icons/PictureAsPdfTwoTone';
import '@trendmicro/react-sidenav/dist/react-sidenav.css';

class SideBar extends Component {
    render() {
        return <SideNav
            onSelect={this.props.onSelect}
        >
            <SideNav.Toggle/>
            <SideNav.Nav defaultSelected="home">
                <NavItem eventKey="home">
                    <NavIcon>
                        <HomeTwoToneIcon/>
                    </NavIcon>
                    <NavText>
                        Home
                    </NavText>
                </NavItem>
                <NavItem eventKey="resume">
                    <NavIcon>
                        <PictureAsPdfTwoToneIcon/>
                    </NavIcon>
                    <NavText>
                        Resume
                    </NavText>
                </NavItem>
                <NavItem eventKey="algovisual">
                    <NavIcon>
                        <PictureAsPdfTwoToneIcon/>
                    </NavIcon>
                    <NavText>
                        AlgoVisual
                    </NavText>
                </NavItem>
            </SideNav.Nav>
        </SideNav>;
    }
}

export {SideBar}