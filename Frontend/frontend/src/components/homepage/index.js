import React, { useState, useEffect } from 'react';
import { connect } from "react-redux";

// import reducers here

const Homepage = () => {
    return (
        <React.Fragment>
            {/* homepage component goes here */}
        </React.Fragment>
    )
}

const mapStateToProps = (state) => {
    return {
        // map state to props here for reducers
    }
}

export default connect(mapStateToProps, {
    // add reducers here
})(Homepage);