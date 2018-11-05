<template>
    <b-row>
        <b-col col cols="3" md="4">
            <label for="description-input">Kuvaus</label>
        </b-col>
        <b-col col cols="9" md="8">
            <b-form-textarea
                id="description-input"
                type="text"
                rows="4"
                :value="value"
                required
                @input="input"
            />
        </b-col>
    </b-row>
</template>
<script>
export default {
    props: ['value'],
    methods: {
        input(value) {
            this.$emit('input', value);
        },
    },
};
</script>
