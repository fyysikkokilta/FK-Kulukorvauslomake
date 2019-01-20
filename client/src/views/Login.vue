<template>
  <b-modal
    ref="modal"
    @hide="close"
    @cancel="close"
    @ok="submit"
    :ok-disabled="!valid"
    ok-title="Kirjaudu!"
    cancel-title="Peruuta."
    centered
  >
    <template slot="modal-header">
      <h3>Kirjaudu sisään</h3>
    </template>
    <b-alert variant="danger" :show="!!error">{{ error }}</b-alert>
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
import { mapActions, mapState } from 'vuex';
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
    close(ev) {
      // TODO use modals hidden event
      // Don't close after failed submit
      if (ev.defaultPrevented) return;
      // Hmm, wait for animation
      setTimeout(() => this.$router.push('/'), 500);
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
