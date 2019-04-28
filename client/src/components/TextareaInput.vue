<template>
  <b-row style="margin-top: 5px;">
    <b-col col cols="3" md="4">
      <label for="route-input">{{ header }}</label>
    </b-col>
    <b-col col cols="9" md="8">
      <b-form-textarea
        id="route-input"
        type="text"
        :rows="rows"
        :value="value"
        required
        @input="input"
      />
    </b-col>
  </b-row>
</template>
<script>
export default {
  props: ['value', 'header', 'rows'],
  methods: {
    input(value) {
      this.$emit('input', value);
    },
  },
};
</script>
