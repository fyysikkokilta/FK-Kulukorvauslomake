<template>
  <b-form>
    <br>
    <NameInput v-model="form.name"/>
    <IbanInput v-model="form.iban"/>
    <TextareaInput header="Kuvaus" rows="4" v-model="form.description" @input="egg"/>
    <hr>
    <ExplanationsInput v-model="form.explanations"/>
    <hr>
    <ReceiptsInput v-model="form.receipts"/>
    <hr>
    <SubmitButton @submit="submit"/>
  </b-form>
</template>
<script>
import { mapActions } from 'vuex';

import NameInput from '@/components/NameInput.vue';
import IbanInput from '@/components/IbanInput.vue';
import TextareaInput from '@/components/TextareaInput.vue';
import ExplanationsInput from '@/components/ExplanationsInput.vue';
import ReceiptsInput from '@/components/ReceiptsInput.vue';
import SubmitButton from '@/components/SubmitButton.vue';

export default {
  components: {
    NameInput,
    IbanInput,
    TextareaInput,
    ExplanationsInput,
    ReceiptsInput,
    SubmitButton,
  },
  data() {
    return {
      form: {
        name: '',
        iban: '',
        description: '',
        explanations: [],
        receipts: [],
      },
    };
  },
  methods: {
    ...mapActions(['sendCostReimbursement']),
    egg(value) {
      const body = document.getElementsByTagName('body')[0];
      if (value.toLowerCase().includes('come to the dark side')) {
        document.documentElement.style.filter = 'invert(100%)';
        body.style.background = 'black';
      }
    },
    submit() {
      const desc = this.form.description.toLowerCase();
      if (desc === 'do a barrel roll') {
        const body = document.getElementsByTagName('body')[0];
        body.className = 'roll';

        setTimeout(() => {
          body.className = '';
        }, 3000);

        return;
      }

      this.sendCostReimbursement(this.form);
    },
  },
};
</script>
<style lang="scss">
body.roll {
  animation: barrelroll 3s ease-in-out;
}

@keyframes barrelroll {
  0% {
    transform: rotate(0deg);
  }
  25% {
    transform: rotate(90deg);
  }
  50% {
    transform: rotate(180deg);
  }
  75% {
    transform: rotate(270deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
