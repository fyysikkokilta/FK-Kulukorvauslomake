export async function getUser() {
    return fetch('/api/users/me');
}

export async function login(email, password) {
    return fetch('/api/users/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    });
}

export async function register(email, password) {
    return fetch('/api/users/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    });
}

export async function getReimbursements(search = {}) {
    return fetch(
        `/api/reimbursements?${new URLSearchParams(search).toString()}`,
    );
}

export async function getPDF(uuid) {
    return fetch(`/api/reimbursements/${uuid}/pdf`);
}

export async function getAllPDFs(search = {}) {
    return fetch(
        `/api/reimbursements/pdfs?${new URLSearchParams(search).toString()}`,
    );
}

export async function sendCostReimbursement(form) {
    return fetch('/api/reimbursements/cost', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(form),
    });
}

export async function sendTravelReimbursement(form) {
    return fetch('/api/reimbursements/travel', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(form),
    });
}
