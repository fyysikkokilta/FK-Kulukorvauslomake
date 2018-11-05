<template>
    <b-form>
        <br>
        <NameInput v-model="form.name" />
        <IbanInput v-model="form.iban" />
        <DescriptionInput v-model="form.description" />
        <hr />
        <ExplanationsInput v-model="form.explanations" />
        <hr />
        <SubmitButton @submit="submit" />
    </b-form>
</template>
<script>
import NameInput from '@/components/NameInput.vue';
import IbanInput from '@/components/IbanInput.vue';
import DescriptionInput from '@/components/DescriptionInput.vue';
import ExplanationsInput from '@/components/ExplanationsInput.vue';
import SubmitButton from '@/components/SubmitButton.vue';

export default {
    components: {
        NameInput,
        IbanInput,
        DescriptionInput,
        ExplanationsInput,
        SubmitButton,
    },
    data() {
        return {
            form: {
                name: '',
                iban: '',
                description: '',
                explanations: [],
            },
        };
    },
    methods: {
        submit() {
            console.log(this.$refs);
            console.log({ ...this.form });
        },
    },
};
</script>
