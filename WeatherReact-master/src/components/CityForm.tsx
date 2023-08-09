import * as React from "react";

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import FormSelect from "react-bootstrap/FormSelect";

import "../styles/CityForm.css";


function CityForm(props) {
    const cities = ['Abu Dhabi','Amsterdam','Ankara','Ashgabat','Astana','Athens','Baku','Bangkok','Beijing','Belgrade',
        'Berlin','Brasília','Brussels','Cairo','Canberra','Colombo','Copenhagen','Dublin','Havana','Helsinki','Jakarta',
        'Jerusalem','Kyiv','Lima','Lisbon','London','Luxembourg','Madrid','Minsk','Moscow','New Delhi','Ottawa','Paris',
        'Prague','Riga','Rome','Seoul','Singapore','Stockholm','Tallinn','Tbilisi','Tokyo','Vienna','Warsaw',
        'Washington']

    return (
        <Form onSubmit={props.getWeather}>
            <h6>Select City</h6>
            <FormSelect name="city">
                {cities.map((city) => (
                    <option key={city} value={city}>
                        {city}
                    </option>
                ))}
            </FormSelect>
            <Button type='submit' variant="info" onClick={() => props.setDays(1)}>Get 24 hours</Button>
            <Button type='submit' variant="info" onClick={() => props.setDays(5)}>Get 5 days</Button>
        </Form>
    );
}

export default CityForm;