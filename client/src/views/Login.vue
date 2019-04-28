<template>
  <b-modal
    ref="modal"
    @hidden="closed"
    @ok="submit"
    :ok-disabled="!valid"
    ok-title="Kirjaudu!"
    cancel-title="Peruuta."
    centered
  >
    <template slot="modal-header">
      <h3>Kirjaudu sisään</h3>
    </template>
    <b-alert class="login-alert" variant="danger" show v-if="!!error">{{ error }}</b-alert>
    <form @submit.stop.prevent="submit">
      <b-row>
        <b-col col cols="3" md="4">
          <label for="login-email">Sähköposti</label>
        </b-col>
        <b-col col cols="9" md="8">
          <b-form-input v-model="email" id="login-email" :state="emailState"/>
        </b-col>
      </b-row>
      <b-row>
        <b-col col cols="3" md="4">
          <label for="login-password">Salasana</label>
        </b-col>
        <b-col col cols="9" md="8">
          <b-form-input
            v-model="password"
            id="login-password"
            :state="passwordState"
            type="password"
          />
        </b-col>
      </b-row>
      <!-- Enable submit by hitting enter -->
      <button type="submit" hidden :disabled="!valid"/>
    </form>
  </b-modal>
</template>
<script>
import { mapActions, mapState, mapMutations } from 'vuex';
export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  mounted() {
    if (this.user) {
      this.close();
      this.$router.replace({ name: 'home' });
      return;
    }
    this.$refs.modal.show();
  },
  computed: {
    ...mapState(['user', 'error', 'loading']),
    passwordState() {
      return this.password.length > 3;
    },
    emailState() {
      return this.email.length > 3;
    },
    valid() {
      return this.emailState && this.passwordState;
    },
  },
  methods: {
    ...mapActions(['login']),
    ...mapMutations(['CLEAR_ERROR']),
    closed() {
      this.CLEAR_ERROR();
      this.$router.push('/');
    },
    submit(ev) {
      // ev is native event when called from button
      // and BvEvent when called from modal
      ev.preventDefault();

      const { email, password } = this;
      this.login({ email, password });
    },
  },
};
</script>
<style scoped>
.login-alert {
  animation: shake 0.5s;
}

@keyframes shake {
  0% {
    transform: translate(1px, 1px) rotate(0deg);
  }
  10% {
    transform: translate(-1px, -2px) rotate(-1deg);
  }
  20% {
    transform: translate(-3px, 0px) rotate(1deg);
  }
  30% {
    transform: translate(3px, 2px) rotate(0deg);
  }
  40% {
    transform: translate(1px, -1px) rotate(1deg);
  }
  50% {
    transform: translate(-1px, 2px) rotate(-1deg);
  }
  60% {
    transform: translate(-3px, 1px) rotate(0deg);
  }
  70% {
    transform: translate(3px, 1px) rotate(-1deg);
  }
  80% {
    transform: translate(-1px, -1px) rotate(1deg);
  }
  90% {
    transform: translate(1px, 2px) rotate(0deg);
  }
  100% {
    transform: translate(1px, -2px) rotate(-1deg);
  }
}
</style>
