<script setup>
import { ref } from "vue";

function registerUser(event){
  window.location.href = '/register'
}

</script>

<template>
    <div class="container">
        <div class="photogram_photo_div">
          <!-- <img alt="Photogram photo" class="photogram_photo" src="../images/under_pier.jpg" width="200px" height="200px" /> -->
        </div>
        <div class="login_div">
          <div class="title">
            <img alt="photogram logo" class="photogram_logo" src="../images/igicon.svg" width="20px" height="20px"/>
            <h1 class="login_title">Photogram</h1>
          </div>
          <hr>
          <div class="body">
            <p>Share photos of your favourite moments with friends, family and the world
            </p>
            <div class="body_buttons">
              <button id="register_button" v-on:click="registerUser">Register</button>
              <button id="login_button">Login</button>
            </div>
          </div>
        </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 250px;
  margin-top: 100px;
}

.photogram_photo_div {
  border-radius: 10px;
  width: 25%;
  height: 90%;
  background-image: url(../images/under_pier.jpg);
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  margin-right: 10px;
  box-shadow: 7px 7px 4px rgba(0, 0, 0, 0.25);

}

hr {
  width: 70%;
  background-color: grey;
  margin-left: auto;
  margin-right: auto;
  margin-top: 0px;
}

.login_div {
  border: 0.5px solid grey;
  border-radius: 10px;
  background-color: white;
  width: 45%;
  height: 90%;
  box-shadow: 7px 7px 4px rgba(0, 0, 0, 0.25);
}

.title {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 25px 15px;
  height: 20%;
}

.title h1 {
  font-size: 26px;
  font-family: fantasy;
  margin-left: 5px;
}

.body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 10px 10px;
}

.body_buttons {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 5px 5px;
  width: 50%;
  margin-top: 15px;
}

.body_buttons button {
  width: 100px;
  height: 30px;
  color: white;
  font-weight: bold;
  font-size: 14px;
  border-radius: 5px;
  text-align: center;
}

#register_button {
  background-color: rgb(40, 197, 40);
  border: 1px solid rgb(40, 197, 40);
}

#login_button {
  background-color: rgb(63, 63, 184);
  border: 1px solid rgb(63, 63, 184);
}

#register_button:hover {
  background-color: rgb(80, 255, 80);
  border: 1px solid rgb(80, 255, 80);
}

#register_button:active {
  background-color: rgb(18, 156, 18);
  border: 1px solid rgb(18, 156, 18);
}

#login_button:hover {
  background-color: rgb(83, 83, 248);
  border: 1px solid rgb(83, 83, 248);
}

#login_button:active {
  background-color: rgb(49, 49, 156);
  border: 1px solid rgb(49, 49, 156);
}



</style>