import React, {Component} from "react";
import Header from "./Header";
import MainContent from "./MainContent";
import '../styles/appStyle.css';

export default class App extends Component {
    render() {
        return (
            <div className="container"
            >
                <Header />
                <MainContent />
                <nav className="navbar-footer">
                </nav>
            </div>
        );
    }
}