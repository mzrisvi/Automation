import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
    await page.goto('https://todomvc.com/');
    await expect(page.getByRole('tooltip', { name: 'Website React is a JavaScript' })).toBeVisible();

    await page.getByRole('link', { name: 'React New', exact: true }).click();
    await page.getByTestId('text-input').fill('buy grocery');
    await page.getByTestId('text-input').press('Enter');
    await page.getByTestId('text-input').fill('go for walk');
    await page.getByTestId('text-input').press('Enter');
    await page.getByTestId('text-input').fill('play');
    await page.getByTestId('text-input').press('Enter');
    await expect(page.getByRole('button', { name: '×' })).toBeVisible();

    await page.getByRole('listitem').filter({ hasText: 'buy grocery' }).getByTestId('todo-item-toggle').check();
    await page.getByRole('listitem').filter({ hasText: 'play' }).getByTestId('todo-item-toggle').check();
    await page.getByRole('link', { name: 'Completed' }).click();
    await page.getByRole('link', { name: 'Active' }).click();
    await expect(page.getByTestId('todo-item-label')).toBeVisible();
    await expect(page.getByRole('link', { name: 'All' })).toBeVisible();
    await page.getByTestId('text-input').click();
    await page.getByRole('button', { name: 'Clear completed' }).click();
    await page.getByRole('link', { name: 'All' }).click();
});