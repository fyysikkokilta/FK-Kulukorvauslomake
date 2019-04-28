import axios from 'axios';

export function me() {
  return axios.get('/api/users/me');
}

export function login(email, password) {
  return axios.post('/api/users/login', { email, password });
}

export function register(email, password) {
  return axios.post('/api/users/register', { email, password });
}

export function getReimbursements(search = {}) {
  return axios.get(
    `/api/reimbursements?${new URLSearchParams(search).toString()}`,
  );
}

export function sendCostReimbursement(form) {
  return axios.post('/api/reimbursements/cost', form);
}

export function sendTravelReimbursement(form) {
  return axios.post('/api/reimbursements/travel', form);
}

export function updateReimbursement(uuid, data) {
  return axios.put(`/api/reimbursements/${uuid}`, data);
}
