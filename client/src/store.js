import Vue from 'vue';
import Vuex from 'vuex';

import * as api from '@/api';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        sending: false,
    },
    mutations: {
        setSending(state, status) {
            state.sending = status;
        },
    },
    actions: {
        async sendCostReimbursement({ commit }, form) {
            commit('setSending', { status: true });

            // Hyhhyh
            const receipts = await Promise.all(
                form.receipts.map(
                    r =>
                        new Promise(resolve => {
                            const fr = new FileReader();

                            fr.onload = e => {
                                resolve({
                                    content: e.target.result,
                                    originalName: r.name,
                                });
                            };
                            fr.readAsDataURL(r);
                        }),
                ),
            );

            console.log(receipts);

            const explanations = form.explanations.map(exp => ({
                explanation: exp.explanation,
                amount: exp.amount,
            }));

            const transformedForm = {
                ...form,
                receipts,
                explanations,
            };

            const resp = await api.sendCostReimbursement(transformedForm);
            console.log(resp);

            commit('setSending', { status: false });
        },
    },
});
