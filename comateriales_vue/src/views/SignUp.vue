<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Registro de cuenta</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Usuario</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Clave</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repita Clave</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <!-- <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div> -->

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Registrar</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/log-in">Si tiene cuenta, click aqui</router-link> para ingresar!
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from "axios";

export default {
  name: "SignUp",

  data: function () {
    return {
      user: {
        username: "",
        password: "",
        name: "",
        email: "",
        account: {
          lastChangeDate: new Date().toJSON().toString(),
          balance: 0,
          isActive: true,
        },
      },
    };
  },

  methods: {
    processSignUp: function () {
      axios
        .post("https://comateriales-be.herokuapp.com/user/", this.user, {
          headers: {},
        })
        .then((result) => {
          let dataSignUp = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };

          this.$emit("completedSignUp", dataSignUp);
        })
        .catch((error) => {
          console.log(error);
          alert("Error en el resgistro.");
        });
    },
  },
};
</script>