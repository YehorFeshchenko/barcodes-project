import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import AllComponents from './components/AllComponents';
import AddComponent from './components/AddComponent';
import SearchComponent from './components/SearchComponent';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar, Nav} from 'react-bootstrap';
import './App.css';


function App() {
    return (
        <Router>
            <div>
                <Navbar className="navbar-custom" expand="lg">
                    <Navbar.Brand href="#home">My App</Navbar.Brand>
                    <Nav className="mr-auto">
                        <Nav.Link href="/">All Components</Nav.Link>
                        <Nav.Link href="/add">Add Component</Nav.Link>
                        <Nav.Link href="/search">Search</Nav.Link>
                    </Nav>
                </Navbar>
                <Routes>
                    <Route path="/" element={<AllComponents/>}/>
                    <Route path="/add" element={<AddComponent/>}/>
                    <Route path="/search" element={<SearchComponent/>}/>
                </Routes>
            </div>
        </Router>
    );
}

export default App;
