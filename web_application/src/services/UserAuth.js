const UserAuth = {
    isAuthenticated: localStorage.getItem('isAuthenticated') === null
        ? 'false'
        : localStorage.getItem('isAuthenticated'),

    authenticate(cb) {
        this.isAuthenticated = 'true';
        localStorage.setItem('isAuthenticated', 'true');
        setTimeout(cb, 100)
    },

    signout(cb) {
        this.isAuthenticated = 'false';
        localStorage.setItem('isAuthenticated', 'false');
        setTimeout(cb, 100)
    }
};

export default UserAuth;
