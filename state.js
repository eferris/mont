const appStatus = '';
window.appStatus = appStatus;

export const stateTeacher = {
    data: [],
    container: null,
    setOptions(newOptions) {
        this.data = newOptions;
    },
    getOptions() {
        return(this.data);
    }
}


export const stateStudent = {
    data: [],
    container: null,
    setOptions(newOptions) {
        this.data = newOptions;
    },
    getOptions() {
        return(this.data);
    }
}

export const stateLesson = {
    data: [],
    container: null,
    setOptions(newOptions) {
        this.data = newOptions;
    },
    getOptions() {
        return(this.data);
    }
}

export const stateSubject = {
    data: [],
    container: null,
    setOptions(newOptions) {
        this.data = newOptions;
    },
    getOptions() {
        return(this.data);
    }
}
