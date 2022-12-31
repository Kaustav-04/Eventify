import React from "react";
import { useSelector } from "react-redux";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faAsterisk } from "@fortawesome/free-solid-svg-icons";
import Logo from "../../images/Eventlabs/FormLogo.png";
import { forwardRef } from "react";
import { useState } from "react";

const Question = (props) => {
  const [id, setId] = useState(null);
  const changeHandler = (e) => {
    props.setvalue({ ...props.value, id: e.target.value });
  };
  return (
    <div
      className="flex flex-col p-10 my-6 bg-transparent rounded-3xl"
      id={props.id}
    >
      <label
        htmlFor={props.id}
        className="px-2 flex justify-between items-center mb-4"
      >
        <span className="text-4xl mr-3">{props.label}</span>
        <span className="text-xl text-[#ff0000]">
          <FontAwesomeIcon icon={faAsterisk} />
        </span>
      </label>
      {props.type === "textArea" ? (
        <textarea
          className="border-[#000030] border-b text-3xl p-4 h-fit rounded-xl focus:border-[#00000030] focus:border-b"
          id={props.id}
          required={props.required === "true"}
          placeholder={props.placeholder}
        />
      ) : (
        <input
          type="text"
          className="border-[#000000] border-b text-3xl p-4 h-fit rounded-xl focus:border-[#00000030] focus:border-b"
          name=""
          id={props.id}
          required={props.required === "true"}
          placeholder={props.placeholder}
          onChange={changeHandler}
        />
      )}
    </div>
  );
};

const ParticipantForm = () => {
  const QuestionList = useSelector((state) => state.question.questions);
  const [value, setValue] = useState({
    Q1: "",
    Q2: "",
    Q3: "",
    Q4: "",
    Q5: "",
    Q6: "",
    Q7: "",
    Q8: "",
    Q9: "",
    Q10: "",
    Q11: "",
    Q12: "",
    Q13: "",
    Q14: "",
    Q15: "",
  });
  const sendParticipateDetails = () => {
    sendDatails();
  };

  const sendDatails = async () => {
    const Response = await fetch("/participant", {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({
        name: value.Q1,
        email: value.Q2,
        phone: value.Q3,
        walletaddress: value.Q4,
        address: value.Q5,
        Q1: value.Q6,
        Q2: value.Q7,
        Q3: value.Q8,
        Q4: value.Q9,
        Q5: value.Q10,
        Q6: value.Q11,
        Q7: value.Q12,
        Q8: value.Q13,
        Q9: value.Q14,
        Q10: value.Q15,
      }),
    });
  };

  return (
    <div className="w-screen h-screen flex flex-wrap items-center justify-around bg-[#000000] text-white overflow-hidden">
      <div className="w-1/4">
        <img src={Logo} className="w-full h-full" alt="eventLabs" />
      </div>
      <div className="w-1/2 h-screen flex flex-col overflow-y-auto scrollbar-none">
        <div className="flex flex-col p-10 my-6 bg-transparent items-center  rounded-3xl">
          <h1 className="text-5xl font-bold text-center mb-6">Event Name</h1>
          <h1 className="text-3xl font-medium text-center mb-6">
            Participants Registration Form
          </h1>
          <p className="text-2xl font-normal text-justify mb-6">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Vero,
            rerum repellat? Voluptate, quae alias! Non modi sapiente quo
            incidunt ducimus quasi soluta maiores reiciendis quas distinctio a
            vero cupiditate maxime earum qui, sint totam repellat quam eveniet
            veritatis eligendi nulla minus nam nostrum! Nihil ea ex ipsa vitae,
            perspiciatis eaque?
          </p>
          <a href="www.facebook.com" target="_blank">
            www.facebook.com
          </a>
        </div>
        {QuestionList.map((i, index) => (
          <Question
            id={`Q${index + 1}`}
            label={i.name}
            type={i.type}
            required={i.required}
            placeholder={i.placeholder}
            setvalue={setValue}
            value={value}
          />
        ))}
        <button
          onClick={sendParticipateDetails}
          className="text-white rounded-xl bg-[#3361C2] my-7 p-5 text-3xl font-medium m-auto"
        >
          Submit
        </button>
      </div>
    </div>
  );
};

export default ParticipantForm;
