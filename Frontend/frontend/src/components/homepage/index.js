import React from "react";
import "./styles.css";

import {
  Navbar,
  Nav,
  NavDropdown,
  Form,
  FormControl,
  Button,
  Carousel,
} from "react-bootstrap";

// import reducers here

const Homepage = () => {
  return (
    <React.Fragment>
      <div>
        <Navbar bg="light" expand="lg">
          <Navbar.Brand href="#home">Jaisalmer E-Commerce</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link href="#home">Home</Nav.Link>
              <Nav.Link href="#link">Account</Nav.Link>
              <NavDropdown title="Products" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">
                  Electronics
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">Grocery</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">
                  Home Accessories
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.4">Fashion</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.5">Other's</NavDropdown.Item>
              </NavDropdown>
            </Nav>
            <Form inline>
              <FormControl
                type="text"
                placeholder="Search for products"
                className="mr-sm-2"
              />
              <Button variant="outline-success">Search</Button>
            </Form>
          </Navbar.Collapse>
        </Navbar>
      </div>
      <div className="carousel">
        <Carousel>
          <Carousel.Item>
            <img
              className="carousel"
              src="https://source.unsplash.com/random"
              alt="First slide"
            />
            <Carousel.Caption>
              <h3>Promotions</h3>
              <p>view is giving but 1 get 1 free</p>
            </Carousel.Caption>
          </Carousel.Item>
          <Carousel.Item>
            <img
              className="carousel"
              src="https://source.unsplash.com/random"
              alt="Second slide"
            />

            <Carousel.Caption>
              <h3>Discounts</h3>
              <p>Get 50% when bill is more than 1000</p>
            </Carousel.Caption>
          </Carousel.Item>
          <Carousel.Item>
            <img
              className="carousel"
              src="https://source.unsplash.com/random"
              alt="Third slide"
            />

            <Carousel.Caption>
              <h3>Offer's</h3>
              <p>buy two shirts and get one free</p>
            </Carousel.Caption>
          </Carousel.Item>
        </Carousel>
      </div>
    </React.Fragment>
  );
};
export default Homepage;

// const mapStateToProps = (state) => {
//   return {
//     // map state to props here for reducers
//   };
// };

// export default connect(mapStateToProps, {
//   // add reducers here
// })(Homepage);
