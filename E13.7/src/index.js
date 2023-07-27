import './styles.css';
console.log('Привет');

async function refreshUsers(e) {
    const urlUsers = 'api/users/';
    const respUserList = await fetch(urlUsers, {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
    });
    const dataUserList = await respUserList.json();
    const userListOl = document.querySelector('#user-list');
    // reset user list
    userListOl.textContent = '';
    dataUserList.forEach((element) => {
        console.log(`<li>${element.name}</li>`);
        const li = document.createElement('li');
        li.innerHTML = `<b>Пользователь:</b> ${element.name}`;
        li.id = `${element.id}_${element.username}`;

        // li.textContent = `${element.name}`;
        userListOl.append(li);
    });
    console.log(dataUserList);
    document.querySelector('#user-list').value += dataUserList.name + '\n';
}

document.querySelector('#user-list-get').onclick = refreshUsers;
