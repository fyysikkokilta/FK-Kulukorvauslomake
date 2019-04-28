<template>
  <b-form>
    <br>
    <NameInput v-model="form.name"/>
    <IbanInput v-model="form.iban"/>
    <TextareaInput header="Matkan tarkoitus" rows="4" v-model="form.description"/>
    <TextareaInput header="Reitti" rows="2" v-model="form.route"/>
    <TextareaInput header="Kyydissä olleet" rows="2" v-model="form.passengers"/>
    <LicensePlateInput v-model="form.licenseNumber"/>
    <DistanceInput v-model="form.distance"/>
    <hr>
    <SubmitButton @submit="submit"/>
  </b-form>
</template>
<script>
import NameInput from '@/components/NameInput.vue';
import IbanInput from '@/components/IbanInput.vue';
import TextareaInput from '@/components/TextareaInput.vue';
import SubmitButton from '@/components/SubmitButton.vue';
import LicensePlateInput from '@/components/LicensePlateInput.vue';
import DistanceInput from '@/components/DistanceInput.vue';
import { mapActions } from 'vuex';

export default {
  components: {
    NameInput,
    IbanInput,
    TextareaInput,
    SubmitButton,
    LicensePlateInput,
    DistanceInput,
  },
  data() {
    return {
      form: {
        name: '',
        iban: '',
        description: '',
        route: '',
        passengers: '',
        distance: 0,
        licenseNumber: '',
      },
    };
  },
  methods: {
    ...mapActions(['sendTravelReimbursement']),
    submit() {
      const desc = this.form.description.toLowerCase();
      if (desc === 'do a barrel roll') {
        this.form.description = 'no u';

        return;
      }
      this.sendTravelReimbursement(this.form);
    },
  },
};
</script>
