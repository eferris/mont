const appAccount = '';
window.appAccount = appAccount;

export  let myDisplay = {
    container: '',
    typeName: '',
    selectedName: '',
    eligibleBtn: null,
    oldContent: 'Select a student and or a subject. Click "Load Lessons" to display lesson info.'

}

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


export const statePage = {
    data: [],
    container: null,
    setOptions(newOptions) {
        this.data = newOptions;
    },
    getOptions() {
        return(this.data);
    }
}


export const stateCurriculum = {
    data: [],
    container: null,
    setOptions(newOptions) {
        this.data = newOptions;
    },
    getOptions() {
        return(this.data);
    }
}


export const stateMaterial = {
    data: [],
    container: null,
    setOptions(newOptions) {
        this.data = newOptions;
    },
    getOptions() {
        return(this.data);
    }
}


export const statePrerequisite = {
    data: [],
    container: null,
    setOptions(newOptions) {
        this.data = newOptions;
    },
    getOptions() {
        return(this.data);
    }
}


export const statePoster = {
    data: [],
    container: null,
    setOptions(newOptions) {
        this.data = newOptions;
    },
    getOptions() {
        return(this.data);
    }
}