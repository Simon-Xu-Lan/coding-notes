import React from 'react';

function Alert(props) {
  console.log('1', props);

  return (
    <div className={`alert alert-${props.type || 'success'}`} role="alert">
      {props.children}
    </div>
  );
}

export default Alert;
