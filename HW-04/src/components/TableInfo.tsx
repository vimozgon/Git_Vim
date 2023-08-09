import * as React from "react";
import Badge from "react-bootstrap/Badge";


function TableInfo(props) {
    return (
        <>
            <h6>City: <Badge bg="info">{props.name}</Badge></h6>
            <h6>Current date: <Badge bg="info">{props.date}</Badge></h6>
            <h6>Sunrise today: <Badge bg="info">{props.sunrise}</Badge></h6>
            <h6>Sunset today: <Badge bg="info">{props.sunset}</Badge></h6>
        </>
    );
}

export default TableInfo;