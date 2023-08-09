import * as React from "react";

import Badge from "react-bootstrap/Badge";
import Table from "react-bootstrap/Table";
import {Fragment} from "react";

import TableHeader from "./TableHeader";
import TableRow from "./TableRow";
import TableInfo from "./TableInfo";

import "../styles/Forecast.css";


function Forecast(props) {
    let cur_date;   // For daily data output in a 5-day weather table
    return (
        <Fragment>
        { props.info.name &&
            <div>
                <TableInfo
                    name={props.info.name}
                    date={props.info.date}
                    sunrise={props.info.sunrise}
                    sunset={props.info.sunset}
                />
                { props.info.days == 1 ?
                    <Table striped bordered hover className={"forecast"}>
                        <TableHeader />
                        <tbody>
                        { props.forecast.map((timeInterval) =>
                            <TableRow
                                key={timeInterval.dt}
                                time={props.getTime(timeInterval.dt)}
                                temperature={timeInterval.main.temp.toFixed()}
                                cloud={timeInterval.weather[0].description}
                                wind={timeInterval.wind.speed.toFixed()}
                                pressure={props.getmmHG(timeInterval.main.pressure).toFixed()}
                            />
                        )}
                        </tbody>
                    </Table> :
                    <Table bordered hover className={"forecast"}>
                        <TableHeader />
                        <tbody>
                        { props.forecast.map((timeInterval) =>
                            cur_date == props.getDate(timeInterval.dt) ?
                                <TableRow
                                    key={timeInterval.dt}
                                    time={props.getTime(timeInterval.dt)}
                                    temperature={timeInterval.main.temp.toFixed()}
                                    cloud={timeInterval.weather[0].description}
                                    wind={timeInterval.wind.speed.toFixed()}
                                    pressure={props.getmmHG(timeInterval.main.pressure).toFixed()}
                                /> :
                                <Fragment key={timeInterval.dt}>
                                    <tr>
                                        <td colSpan={5}>
                                            <Badge bg="info">Forecast for {cur_date = props.getDate(timeInterval.dt)}</Badge>
                                        </td>
                                    </tr>
                                    <TableRow
                                        time={props.getTime(timeInterval.dt)}
                                        temperature={timeInterval.main.temp.toFixed()}
                                        cloud={timeInterval.weather[0].description}
                                        wind={timeInterval.wind.speed.toFixed()}
                                        pressure={props.getmmHG(timeInterval.main.pressure).toFixed()}
                                    />
                                </Fragment>
                        )}
                        </tbody>
                    </Table>
                }
            </div>
        }
        </Fragment>
    );
}

export default Forecast;