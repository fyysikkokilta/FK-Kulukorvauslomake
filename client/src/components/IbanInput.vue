<template>
  <b-row>
    <b-col col cols="3" md="4">
      <label for="iban-input">IBAN</label>
    </b-col>
    <b-col col cols="9" md="8">
      <b-input
        id="iban-input"
        type="text"
        :value="iban"
        required
        placeholder="FI42 5000 1510 0000 23"
        @input="input"
      />
    </b-col>
  </b-row>
</template>
<script>
export default {
  props: ['value'],
  data() {
    return {
      iban: localStorage.iban,
      error: '',
    };
  },
  methods: {
    input(value) {
      this.$emit('input', value);
      localStorage.iban = value;
    },
  },
};
</script>
