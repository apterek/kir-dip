const h1 = document.getElementById('header__h1');
const search = document.getElementById('search');
const table = document.getElementById('table');

const urlPersonal = 'personal';
const urlUsers = 'users';
const urlCameras = 'cameras';
const urlCabinets = 'cabinets';
const urlTime = 'time';

class Router {
  routes = [];
  mode = null;
  root = '/';

  constructor(options) {
    this.mode = window.history.pushState ? 'history' : 'hash';
    if (options.mode) this.mode = options.mode;
    if (options.root) this.root = options.root;
    this.listen();
  }

  add = (path, cb) => {
    this.routes.push({ path, cb });
    return this;
  };

  remove = (path) => {
    for (let i = 0; i < this.routes.length; i += 1) {
      if (this.routes[i].path === path) {
        this.routes.slice(i, 1);
        return this;
      }
    }
    return this;
  };

  flush = () => {
    this.routes = [];
    return this;
  };

  clearSlashes = (path) =>
    path.toString().replace(/\/$/, '').replace(/^\//, '');

  getFragment = () => {
    let fragment = '';
    if (this.mode === 'history') {
      fragment = this.clearSlashes(
        decodeURI(window.location.pathname + window.location.search)
      );
      fragment = fragment.replace(/\?(.*)$/, '');
      fragment = this.root !== '/' ? fragment.replace(this.root, '') : fragment;
    } else {
      const match = window.location.href.match(/#(.*)$/);
      fragment = match ? match[1] : '';
    }
    return this.clearSlashes(fragment);
  };

  navigate = (path = '') => {
    if (this.mode === 'history') {
      window.history.pushState(null, null, this.root + this.clearSlashes(path));
    } else {
      window.location.href = `${window.location.href.replace(
        /#(.*)$/,
        ''
      )}#${path}`;
    }
    return this;
  };

  listen = () => {
    clearInterval(this.interval);
    this.interval = setInterval(this.interval, 50);
  };

  interval = () => {
    if (this.current === this.getFragment()) return;
    this.current = this.getFragment();

    this.routes.some((route) => {
      const match = this.current.match(route.path);
      if (match) {
        match.shift();
        route.cb.apply({}, match);
        return match;
      }
      return false;
    });
  };
}

const router = new Router({
  mode: 'hash',
  root: '/',
});

router
  .add(/main_page/, () => {
    table.innerHTML = '';
    h1.textContent = 'In-Out status';
    table.style.marginRight = '1rem';
    search.style.display = 'none';
    const resultsTime = getData(urlTime);
    getTableHead(resultsTime);
    getTableBody(resultsTime);
  })
  .add(/cameras_status/, () => {
    table.innerHTML = '';
    h1.textContent = 'Cameras status';
    table.style.marginRight = '30rem';
    search.style.display = '';
    const resultsCamera = getData(urlCameras);
    getTableHead(resultsCamera);
    getTableBody(resultsCamera);
  })
  .add(/cabinets_status/, () => {
    table.innerHTML = '';
    h1.textContent = 'Cabinets status';
    table.style.marginRight = '30rem';
    search.style.display = '';
    const resultsCabinets = getData(urlCabinets);
    getTableHead(resultsCabinets);
    getTableBody(resultsCabinets);
  })
  .add('', () => {
    table.innerHTML = '';
    h1.textContent = 'Personal info';
    table.style.marginRight = '30rem';
    search.style.display = '';
    const resultsPersonal = getData(urlPersonal);
    getTableHead(resultsPersonal);
    getTableBody(resultsPersonal);
  });

async function getData(url) {
  await fetch(`http://192.168.0.101/api/${url}/`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((response) => {
      response.json().then((data) => {
        return data.results;
      });
    })
    .catch((e) => {
      console.log(e);
    });
}

function createCircle(value, tr) {
  const td = document.createElement('td');
  const circle = document.createElement('div');
  circle.style.width = '1rem';
  circle.style.height = '1rem';
  circle.style.margin = '0 auto';
  circle.style.backgroundColor = value ? 'green' : 'red';
  circle.style.borderRadius = '50%';
  td.appendChild(circle);
  tr.appendChild(td);
  return table.appendChild(tr);
}

function createTh(value, tr) {
  const th = document.createElement('th');
  th.innerHTML = value.toString().replaceAll('_', ' ');
  tr.appendChild(th);
  return table.appendChild(tr);
}

function createTd(value, tr) {
  const td = document.createElement('td');
  td.innerHTML = value.toString().replaceAll(',', ' ');
  tr.appendChild(td);
  return table.appendChild(tr);
}

function getTableHead(data) {
  const keys = Object.keys(data[0]);
  const tr = document.createElement('tr');
  keys.forEach((key) => {
    createTh(key, tr);
  });
}

function getTableBody(data) {
  data.forEach((item) => {
    const values = Object.values(item);
    const tr = document.createElement('tr');
    values.forEach((value) => {
      if (typeof value === 'object') {
        const newValue = Object.values(value);
        createTd(newValue, tr);
      } else if (typeof value === 'boolean') {
        createCircle(value, tr);
      } else {
        createTd(value, tr);
      }
    });
  });
}
