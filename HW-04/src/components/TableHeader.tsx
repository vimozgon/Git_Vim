import * as React from "react";


function TableHeader() {
    return (
        <thead>
            <tr>
                <th>Time</th>
                <th>Temperature, С</th>
                <th>Сloudiness</th>
                <th>Wind speed, mps</th>
                <th>Pressure, mm Hg</th>
            </tr>
        </thead>
    );
}

export default TableHeader;