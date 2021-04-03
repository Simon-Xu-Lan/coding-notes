import React from 'react';
import './style.css';

function Card(props) {
  return (
    <div className="card">
      <div className="img-container">
        <img alt={props.figure.name} src={props.figure.src} />
      </div>
      <div className="content">
        <ul>
          <li>
            <strong>Name:</strong> {props.figure.name}
          </li>
          <li>
            <strong>Occupation:</strong> {props.figure.occupation}
          </li>
          <li>
            <strong>Location:</strong> {props.figure.location}
          </li>
        </ul>
      </div>
    </div>
  );
}

export default Card;
