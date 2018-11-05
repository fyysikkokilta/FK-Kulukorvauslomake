<template>
    <b-form>
        <br>
        <NameInput v-model="form.name" />
        <IbanInput v-model="form.iban" />
        <DescriptionInput v-model="form.description" />
        <hr />
        <ExplanationsInput v-model="form.explanations" />
        <hr />
        <ReceiptsInput v-model="form.receipts" />
        <hr />
        <SubmitButton @submit="submit" />
    </b-form>
</template>
<script>
import { mapActions } from 'vuex';

import NameInput from '@/components/NameInput.vue';
import IbanInput from '@/components/IbanInput.vue';
import DescriptionInput from '@/components/DescriptionInput.vue';
import ExplanationsInput from '@/components/ExplanationsInput.vue';
import ReceiptsInput from '@/components/ReceiptsInput.vue';
import SubmitButton from '@/components/SubmitButton.vue';

export default {
    components: {
        NameInput,
        IbanInput,
        DescriptionInput,
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
        submit() {
            this.sendCostReimbursement(this.form);
            console.log(this.sendCostReimbursement);
            console.log({ ...this.form });
        },
    },
};
</script>
