

const e = React.createElement;

class Config-Bar extends React.Component {
	constructor(props) {
		super(props);
		this.state = {};
	}
}




class Config-Button extends React.Compononet {
	constructor(props) {
			super(props);
			this.state = {clicked: false, text: ""};
	}

	setText(value) {
		this.state.text = value;
	}

	setClicked(value) {
		this.state.clicked = value;
	}

	render() {

		return e("button", {onClick: () => this.setClicked(true)}, this.state.text)
	}

}