import React from 'react';

function List(props) {
  let purchased = props.groceries.filter((item) => item.purchased);
  return (
    <ul className="list-group">
      {purchased.map((item) => (
        <li className="list-group-item" key={item.id}>
          {item.name}
        </li>
      ))}
    </ul>
  );
}

export default List;
