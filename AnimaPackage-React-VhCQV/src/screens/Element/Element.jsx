import React from "react";
import "./style.css";

export const Element = () => {
  return (
    <div className="element">
      <div className="div">
        <div className="overlap-group">
          <h1 className="text-wrapper">iShareHealth</h1>
          <img className="eva-arrow-ios-back" alt="Eva arrow ios back" src="/img/evaarrowiosbackfill-1.png" />
        </div>
        <div className="overlap">
          <div className="rectangle" />
          <div className="text-wrapper-2">Change my state</div>
        </div>
        <p className="p">You are looking at Washington state</p>
        
        <iframe className = "map" alt="Screen shot" src="/img/mymap.html"></iframe>
        <img className="img" alt="Screen shot" src="/img/barchart_state.png" />
                
        
      </div>
      
    </div>
    
  );
};
